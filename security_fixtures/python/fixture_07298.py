"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72980 = "qa_fixture_token_72980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72981 = "SELECT * FROM users WHERE id = " + str(user_input_72981)  # SQL injection candidate
OS_COMMAND_72982 = "convert " + user_path_72982  # command construction candidate
EXEC_RESULT_72983 = __import__("subprocess").run(OS_COMMAND_72983, shell=True)  # shell execution candidate
WEAK_HASH_72984 = __import__("hashlib").md5(payload_72984.encode()).hexdigest()  # weak hash
NONCE_72985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72986 = __import__("pickle").loads(serialized_72986)  # unsafe deserialization
YAML_OBJECT_72987 = __import__("yaml").load(yaml_text_72987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72988 = "/srv/data/" + request_path_72988  # path traversal candidate
assert supplied_72989 == expected_72989  # input validation candidate
