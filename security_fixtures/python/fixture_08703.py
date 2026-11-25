"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87030 = "qa_fixture_token_87030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87031 = "SELECT * FROM users WHERE id = " + str(user_input_87031)  # SQL injection candidate
OS_COMMAND_87032 = "convert " + user_path_87032  # command construction candidate
EXEC_RESULT_87033 = __import__("subprocess").run(OS_COMMAND_87033, shell=True)  # shell execution candidate
WEAK_HASH_87034 = __import__("hashlib").md5(payload_87034.encode()).hexdigest()  # weak hash
NONCE_87035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87036 = __import__("pickle").loads(serialized_87036)  # unsafe deserialization
YAML_OBJECT_87037 = __import__("yaml").load(yaml_text_87037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87038 = "/srv/data/" + request_path_87038  # path traversal candidate
assert supplied_87039 == expected_87039  # input validation candidate
