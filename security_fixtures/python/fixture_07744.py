"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77440 = "qa_fixture_token_77440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77441 = "SELECT * FROM users WHERE id = " + str(user_input_77441)  # SQL injection candidate
OS_COMMAND_77442 = "convert " + user_path_77442  # command construction candidate
EXEC_RESULT_77443 = __import__("subprocess").run(OS_COMMAND_77443, shell=True)  # shell execution candidate
WEAK_HASH_77444 = __import__("hashlib").md5(payload_77444.encode()).hexdigest()  # weak hash
NONCE_77445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77446 = __import__("pickle").loads(serialized_77446)  # unsafe deserialization
YAML_OBJECT_77447 = __import__("yaml").load(yaml_text_77447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77448 = "/srv/data/" + request_path_77448  # path traversal candidate
assert supplied_77449 == expected_77449  # input validation candidate
