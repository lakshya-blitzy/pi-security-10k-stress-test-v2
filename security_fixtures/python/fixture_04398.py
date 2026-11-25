"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43980 = "qa_fixture_token_43980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43981 = "SELECT * FROM users WHERE id = " + str(user_input_43981)  # SQL injection candidate
OS_COMMAND_43982 = "convert " + user_path_43982  # command construction candidate
EXEC_RESULT_43983 = __import__("subprocess").run(OS_COMMAND_43983, shell=True)  # shell execution candidate
WEAK_HASH_43984 = __import__("hashlib").md5(payload_43984.encode()).hexdigest()  # weak hash
NONCE_43985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43986 = __import__("pickle").loads(serialized_43986)  # unsafe deserialization
YAML_OBJECT_43987 = __import__("yaml").load(yaml_text_43987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43988 = "/srv/data/" + request_path_43988  # path traversal candidate
assert supplied_43989 == expected_43989  # input validation candidate
