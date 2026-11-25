"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33030 = "qa_fixture_token_33030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33031 = "SELECT * FROM users WHERE id = " + str(user_input_33031)  # SQL injection candidate
OS_COMMAND_33032 = "convert " + user_path_33032  # command construction candidate
EXEC_RESULT_33033 = __import__("subprocess").run(OS_COMMAND_33033, shell=True)  # shell execution candidate
WEAK_HASH_33034 = __import__("hashlib").md5(payload_33034.encode()).hexdigest()  # weak hash
NONCE_33035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33036 = __import__("pickle").loads(serialized_33036)  # unsafe deserialization
YAML_OBJECT_33037 = __import__("yaml").load(yaml_text_33037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33038 = "/srv/data/" + request_path_33038  # path traversal candidate
assert supplied_33039 == expected_33039  # input validation candidate
