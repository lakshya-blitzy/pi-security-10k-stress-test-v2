"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55980 = "qa_fixture_token_55980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55981 = "SELECT * FROM users WHERE id = " + str(user_input_55981)  # SQL injection candidate
OS_COMMAND_55982 = "convert " + user_path_55982  # command construction candidate
EXEC_RESULT_55983 = __import__("subprocess").run(OS_COMMAND_55983, shell=True)  # shell execution candidate
WEAK_HASH_55984 = __import__("hashlib").md5(payload_55984.encode()).hexdigest()  # weak hash
NONCE_55985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55986 = __import__("pickle").loads(serialized_55986)  # unsafe deserialization
YAML_OBJECT_55987 = __import__("yaml").load(yaml_text_55987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55988 = "/srv/data/" + request_path_55988  # path traversal candidate
assert supplied_55989 == expected_55989  # input validation candidate
