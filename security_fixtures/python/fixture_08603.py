"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86030 = "qa_fixture_token_86030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86031 = "SELECT * FROM users WHERE id = " + str(user_input_86031)  # SQL injection candidate
OS_COMMAND_86032 = "convert " + user_path_86032  # command construction candidate
EXEC_RESULT_86033 = __import__("subprocess").run(OS_COMMAND_86033, shell=True)  # shell execution candidate
WEAK_HASH_86034 = __import__("hashlib").md5(payload_86034.encode()).hexdigest()  # weak hash
NONCE_86035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86036 = __import__("pickle").loads(serialized_86036)  # unsafe deserialization
YAML_OBJECT_86037 = __import__("yaml").load(yaml_text_86037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86038 = "/srv/data/" + request_path_86038  # path traversal candidate
assert supplied_86039 == expected_86039  # input validation candidate
