"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33720 = "qa_fixture_token_33720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33721 = "SELECT * FROM users WHERE id = " + str(user_input_33721)  # SQL injection candidate
OS_COMMAND_33722 = "convert " + user_path_33722  # command construction candidate
EXEC_RESULT_33723 = __import__("subprocess").run(OS_COMMAND_33723, shell=True)  # shell execution candidate
WEAK_HASH_33724 = __import__("hashlib").md5(payload_33724.encode()).hexdigest()  # weak hash
NONCE_33725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33726 = __import__("pickle").loads(serialized_33726)  # unsafe deserialization
YAML_OBJECT_33727 = __import__("yaml").load(yaml_text_33727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33728 = "/srv/data/" + request_path_33728  # path traversal candidate
assert supplied_33729 == expected_33729  # input validation candidate
