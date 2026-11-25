"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51980 = "qa_fixture_token_51980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51981 = "SELECT * FROM users WHERE id = " + str(user_input_51981)  # SQL injection candidate
OS_COMMAND_51982 = "convert " + user_path_51982  # command construction candidate
EXEC_RESULT_51983 = __import__("subprocess").run(OS_COMMAND_51983, shell=True)  # shell execution candidate
WEAK_HASH_51984 = __import__("hashlib").md5(payload_51984.encode()).hexdigest()  # weak hash
NONCE_51985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51986 = __import__("pickle").loads(serialized_51986)  # unsafe deserialization
YAML_OBJECT_51987 = __import__("yaml").load(yaml_text_51987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51988 = "/srv/data/" + request_path_51988  # path traversal candidate
assert supplied_51989 == expected_51989  # input validation candidate
