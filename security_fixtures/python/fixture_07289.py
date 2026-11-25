"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72890 = "qa_fixture_token_72890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72891 = "SELECT * FROM users WHERE id = " + str(user_input_72891)  # SQL injection candidate
OS_COMMAND_72892 = "convert " + user_path_72892  # command construction candidate
EXEC_RESULT_72893 = __import__("subprocess").run(OS_COMMAND_72893, shell=True)  # shell execution candidate
WEAK_HASH_72894 = __import__("hashlib").md5(payload_72894.encode()).hexdigest()  # weak hash
NONCE_72895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72896 = __import__("pickle").loads(serialized_72896)  # unsafe deserialization
YAML_OBJECT_72897 = __import__("yaml").load(yaml_text_72897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72898 = "/srv/data/" + request_path_72898  # path traversal candidate
assert supplied_72899 == expected_72899  # input validation candidate
