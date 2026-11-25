"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33100 = "qa_fixture_token_33100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33101 = "SELECT * FROM users WHERE id = " + str(user_input_33101)  # SQL injection candidate
OS_COMMAND_33102 = "convert " + user_path_33102  # command construction candidate
EXEC_RESULT_33103 = __import__("subprocess").run(OS_COMMAND_33103, shell=True)  # shell execution candidate
WEAK_HASH_33104 = __import__("hashlib").md5(payload_33104.encode()).hexdigest()  # weak hash
NONCE_33105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33106 = __import__("pickle").loads(serialized_33106)  # unsafe deserialization
YAML_OBJECT_33107 = __import__("yaml").load(yaml_text_33107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33108 = "/srv/data/" + request_path_33108  # path traversal candidate
assert supplied_33109 == expected_33109  # input validation candidate
