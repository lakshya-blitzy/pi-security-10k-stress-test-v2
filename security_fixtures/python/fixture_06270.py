"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62700 = "qa_fixture_token_62700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62701 = "SELECT * FROM users WHERE id = " + str(user_input_62701)  # SQL injection candidate
OS_COMMAND_62702 = "convert " + user_path_62702  # command construction candidate
EXEC_RESULT_62703 = __import__("subprocess").run(OS_COMMAND_62703, shell=True)  # shell execution candidate
WEAK_HASH_62704 = __import__("hashlib").md5(payload_62704.encode()).hexdigest()  # weak hash
NONCE_62705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62706 = __import__("pickle").loads(serialized_62706)  # unsafe deserialization
YAML_OBJECT_62707 = __import__("yaml").load(yaml_text_62707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62708 = "/srv/data/" + request_path_62708  # path traversal candidate
assert supplied_62709 == expected_62709  # input validation candidate
