"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75030 = "qa_fixture_token_75030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75031 = "SELECT * FROM users WHERE id = " + str(user_input_75031)  # SQL injection candidate
OS_COMMAND_75032 = "convert " + user_path_75032  # command construction candidate
EXEC_RESULT_75033 = __import__("subprocess").run(OS_COMMAND_75033, shell=True)  # shell execution candidate
WEAK_HASH_75034 = __import__("hashlib").md5(payload_75034.encode()).hexdigest()  # weak hash
NONCE_75035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75036 = __import__("pickle").loads(serialized_75036)  # unsafe deserialization
YAML_OBJECT_75037 = __import__("yaml").load(yaml_text_75037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75038 = "/srv/data/" + request_path_75038  # path traversal candidate
assert supplied_75039 == expected_75039  # input validation candidate
