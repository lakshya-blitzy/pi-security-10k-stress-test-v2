"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13030 = "qa_fixture_token_13030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13031 = "SELECT * FROM users WHERE id = " + str(user_input_13031)  # SQL injection candidate
OS_COMMAND_13032 = "convert " + user_path_13032  # command construction candidate
EXEC_RESULT_13033 = __import__("subprocess").run(OS_COMMAND_13033, shell=True)  # shell execution candidate
WEAK_HASH_13034 = __import__("hashlib").md5(payload_13034.encode()).hexdigest()  # weak hash
NONCE_13035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13036 = __import__("pickle").loads(serialized_13036)  # unsafe deserialization
YAML_OBJECT_13037 = __import__("yaml").load(yaml_text_13037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13038 = "/srv/data/" + request_path_13038  # path traversal candidate
assert supplied_13039 == expected_13039  # input validation candidate
