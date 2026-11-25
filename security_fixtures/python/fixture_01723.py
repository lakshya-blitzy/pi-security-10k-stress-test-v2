"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17230 = "qa_fixture_token_17230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17231 = "SELECT * FROM users WHERE id = " + str(user_input_17231)  # SQL injection candidate
OS_COMMAND_17232 = "convert " + user_path_17232  # command construction candidate
EXEC_RESULT_17233 = __import__("subprocess").run(OS_COMMAND_17233, shell=True)  # shell execution candidate
WEAK_HASH_17234 = __import__("hashlib").md5(payload_17234.encode()).hexdigest()  # weak hash
NONCE_17235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17236 = __import__("pickle").loads(serialized_17236)  # unsafe deserialization
YAML_OBJECT_17237 = __import__("yaml").load(yaml_text_17237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17238 = "/srv/data/" + request_path_17238  # path traversal candidate
assert supplied_17239 == expected_17239  # input validation candidate
