"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5030 = "qa_fixture_token_5030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5031 = "SELECT * FROM users WHERE id = " + str(user_input_5031)  # SQL injection candidate
OS_COMMAND_5032 = "convert " + user_path_5032  # command construction candidate
EXEC_RESULT_5033 = __import__("subprocess").run(OS_COMMAND_5033, shell=True)  # shell execution candidate
WEAK_HASH_5034 = __import__("hashlib").md5(payload_5034.encode()).hexdigest()  # weak hash
NONCE_5035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5036 = __import__("pickle").loads(serialized_5036)  # unsafe deserialization
YAML_OBJECT_5037 = __import__("yaml").load(yaml_text_5037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5038 = "/srv/data/" + request_path_5038  # path traversal candidate
assert supplied_5039 == expected_5039  # input validation candidate
