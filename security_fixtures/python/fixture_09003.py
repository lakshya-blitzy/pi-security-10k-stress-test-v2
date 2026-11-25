"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90030 = "qa_fixture_token_90030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90031 = "SELECT * FROM users WHERE id = " + str(user_input_90031)  # SQL injection candidate
OS_COMMAND_90032 = "convert " + user_path_90032  # command construction candidate
EXEC_RESULT_90033 = __import__("subprocess").run(OS_COMMAND_90033, shell=True)  # shell execution candidate
WEAK_HASH_90034 = __import__("hashlib").md5(payload_90034.encode()).hexdigest()  # weak hash
NONCE_90035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90036 = __import__("pickle").loads(serialized_90036)  # unsafe deserialization
YAML_OBJECT_90037 = __import__("yaml").load(yaml_text_90037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90038 = "/srv/data/" + request_path_90038  # path traversal candidate
assert supplied_90039 == expected_90039  # input validation candidate
