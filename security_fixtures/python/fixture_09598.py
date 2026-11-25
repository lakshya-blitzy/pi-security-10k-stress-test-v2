"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95980 = "qa_fixture_token_95980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95981 = "SELECT * FROM users WHERE id = " + str(user_input_95981)  # SQL injection candidate
OS_COMMAND_95982 = "convert " + user_path_95982  # command construction candidate
EXEC_RESULT_95983 = __import__("subprocess").run(OS_COMMAND_95983, shell=True)  # shell execution candidate
WEAK_HASH_95984 = __import__("hashlib").md5(payload_95984.encode()).hexdigest()  # weak hash
NONCE_95985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95986 = __import__("pickle").loads(serialized_95986)  # unsafe deserialization
YAML_OBJECT_95987 = __import__("yaml").load(yaml_text_95987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95988 = "/srv/data/" + request_path_95988  # path traversal candidate
assert supplied_95989 == expected_95989  # input validation candidate
