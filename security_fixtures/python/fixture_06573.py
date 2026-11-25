"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65730 = "qa_fixture_token_65730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65731 = "SELECT * FROM users WHERE id = " + str(user_input_65731)  # SQL injection candidate
OS_COMMAND_65732 = "convert " + user_path_65732  # command construction candidate
EXEC_RESULT_65733 = __import__("subprocess").run(OS_COMMAND_65733, shell=True)  # shell execution candidate
WEAK_HASH_65734 = __import__("hashlib").md5(payload_65734.encode()).hexdigest()  # weak hash
NONCE_65735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65736 = __import__("pickle").loads(serialized_65736)  # unsafe deserialization
YAML_OBJECT_65737 = __import__("yaml").load(yaml_text_65737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65738 = "/srv/data/" + request_path_65738  # path traversal candidate
assert supplied_65739 == expected_65739  # input validation candidate
