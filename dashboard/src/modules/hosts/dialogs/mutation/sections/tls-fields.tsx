import { AllowInsecureField, AlpnField } from "../fields";
import { SettingSection } from "@marzneshin/modules/hosts/components";
import { useTranslation } from "react-i18next";
import { FC } from "react";
import { ClearableTextField } from "@marzneshin/common/components";

export const TlsFields: FC = () => {
    const { t } = useTranslation();
    return (
        <SettingSection
            value="tls-settings"
            triggerText={t("page.hosts.tls-config")}
        >
            <ClearableTextField name="sni" label={t("sni")} />
            <AlpnField />
            <ClearableTextField name="reality_spx" label={t("reality-spx")} />
            <ClearableTextField
                name="encryption"
                label={t("vless-encryption")}
            />
            <AllowInsecureField />
        </SettingSection>
    );
};
