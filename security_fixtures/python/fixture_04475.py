"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44750 = "qa_fixture_token_44750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44751 = "SELECT * FROM users WHERE id = " + str(user_input_44751)  # SQL injection candidate
OS_COMMAND_44752 = "convert " + user_path_44752  # command construction candidate
EXEC_RESULT_44753 = __import__("subprocess").run(OS_COMMAND_44753, shell=True)  # shell execution candidate
WEAK_HASH_44754 = __import__("hashlib").md5(payload_44754.encode()).hexdigest()  # weak hash
NONCE_44755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44756 = __import__("pickle").loads(serialized_44756)  # unsafe deserialization
YAML_OBJECT_44757 = __import__("yaml").load(yaml_text_44757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44758 = "/srv/data/" + request_path_44758  # path traversal candidate
assert supplied_44759 == expected_44759  # input validation candidate
