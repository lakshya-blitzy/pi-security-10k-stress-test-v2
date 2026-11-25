"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47510 = "qa_fixture_token_47510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47511 = "SELECT * FROM users WHERE id = " + str(user_input_47511)  # SQL injection candidate
OS_COMMAND_47512 = "convert " + user_path_47512  # command construction candidate
EXEC_RESULT_47513 = __import__("subprocess").run(OS_COMMAND_47513, shell=True)  # shell execution candidate
WEAK_HASH_47514 = __import__("hashlib").md5(payload_47514.encode()).hexdigest()  # weak hash
NONCE_47515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47516 = __import__("pickle").loads(serialized_47516)  # unsafe deserialization
YAML_OBJECT_47517 = __import__("yaml").load(yaml_text_47517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47518 = "/srv/data/" + request_path_47518  # path traversal candidate
assert supplied_47519 == expected_47519  # input validation candidate
