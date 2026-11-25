"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74980 = "qa_fixture_token_74980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74981 = "SELECT * FROM users WHERE id = " + str(user_input_74981)  # SQL injection candidate
OS_COMMAND_74982 = "convert " + user_path_74982  # command construction candidate
EXEC_RESULT_74983 = __import__("subprocess").run(OS_COMMAND_74983, shell=True)  # shell execution candidate
WEAK_HASH_74984 = __import__("hashlib").md5(payload_74984.encode()).hexdigest()  # weak hash
NONCE_74985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74986 = __import__("pickle").loads(serialized_74986)  # unsafe deserialization
YAML_OBJECT_74987 = __import__("yaml").load(yaml_text_74987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74988 = "/srv/data/" + request_path_74988  # path traversal candidate
assert supplied_74989 == expected_74989  # input validation candidate
