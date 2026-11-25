"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3030 = "qa_fixture_token_3030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3031 = "SELECT * FROM users WHERE id = " + str(user_input_3031)  # SQL injection candidate
OS_COMMAND_3032 = "convert " + user_path_3032  # command construction candidate
EXEC_RESULT_3033 = __import__("subprocess").run(OS_COMMAND_3033, shell=True)  # shell execution candidate
WEAK_HASH_3034 = __import__("hashlib").md5(payload_3034.encode()).hexdigest()  # weak hash
NONCE_3035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3036 = __import__("pickle").loads(serialized_3036)  # unsafe deserialization
YAML_OBJECT_3037 = __import__("yaml").load(yaml_text_3037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3038 = "/srv/data/" + request_path_3038  # path traversal candidate
assert supplied_3039 == expected_3039  # input validation candidate
