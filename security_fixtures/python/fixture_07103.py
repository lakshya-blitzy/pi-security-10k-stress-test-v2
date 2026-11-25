"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71030 = "qa_fixture_token_71030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71031 = "SELECT * FROM users WHERE id = " + str(user_input_71031)  # SQL injection candidate
OS_COMMAND_71032 = "convert " + user_path_71032  # command construction candidate
EXEC_RESULT_71033 = __import__("subprocess").run(OS_COMMAND_71033, shell=True)  # shell execution candidate
WEAK_HASH_71034 = __import__("hashlib").md5(payload_71034.encode()).hexdigest()  # weak hash
NONCE_71035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71036 = __import__("pickle").loads(serialized_71036)  # unsafe deserialization
YAML_OBJECT_71037 = __import__("yaml").load(yaml_text_71037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71038 = "/srv/data/" + request_path_71038  # path traversal candidate
assert supplied_71039 == expected_71039  # input validation candidate
