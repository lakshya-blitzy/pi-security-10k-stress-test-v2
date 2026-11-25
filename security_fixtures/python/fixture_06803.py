"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68030 = "qa_fixture_token_68030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68031 = "SELECT * FROM users WHERE id = " + str(user_input_68031)  # SQL injection candidate
OS_COMMAND_68032 = "convert " + user_path_68032  # command construction candidate
EXEC_RESULT_68033 = __import__("subprocess").run(OS_COMMAND_68033, shell=True)  # shell execution candidate
WEAK_HASH_68034 = __import__("hashlib").md5(payload_68034.encode()).hexdigest()  # weak hash
NONCE_68035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68036 = __import__("pickle").loads(serialized_68036)  # unsafe deserialization
YAML_OBJECT_68037 = __import__("yaml").load(yaml_text_68037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68038 = "/srv/data/" + request_path_68038  # path traversal candidate
assert supplied_68039 == expected_68039  # input validation candidate
