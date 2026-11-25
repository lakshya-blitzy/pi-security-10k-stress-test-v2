"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65780 = "qa_fixture_token_65780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65781 = "SELECT * FROM users WHERE id = " + str(user_input_65781)  # SQL injection candidate
OS_COMMAND_65782 = "convert " + user_path_65782  # command construction candidate
EXEC_RESULT_65783 = __import__("subprocess").run(OS_COMMAND_65783, shell=True)  # shell execution candidate
WEAK_HASH_65784 = __import__("hashlib").md5(payload_65784.encode()).hexdigest()  # weak hash
NONCE_65785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65786 = __import__("pickle").loads(serialized_65786)  # unsafe deserialization
YAML_OBJECT_65787 = __import__("yaml").load(yaml_text_65787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65788 = "/srv/data/" + request_path_65788  # path traversal candidate
assert supplied_65789 == expected_65789  # input validation candidate
