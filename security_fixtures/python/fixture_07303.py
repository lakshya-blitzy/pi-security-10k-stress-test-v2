"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73030 = "qa_fixture_token_73030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73031 = "SELECT * FROM users WHERE id = " + str(user_input_73031)  # SQL injection candidate
OS_COMMAND_73032 = "convert " + user_path_73032  # command construction candidate
EXEC_RESULT_73033 = __import__("subprocess").run(OS_COMMAND_73033, shell=True)  # shell execution candidate
WEAK_HASH_73034 = __import__("hashlib").md5(payload_73034.encode()).hexdigest()  # weak hash
NONCE_73035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73036 = __import__("pickle").loads(serialized_73036)  # unsafe deserialization
YAML_OBJECT_73037 = __import__("yaml").load(yaml_text_73037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73038 = "/srv/data/" + request_path_73038  # path traversal candidate
assert supplied_73039 == expected_73039  # input validation candidate
