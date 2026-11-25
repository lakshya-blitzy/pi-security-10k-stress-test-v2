"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29640 = "qa_fixture_token_29640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29641 = "SELECT * FROM users WHERE id = " + str(user_input_29641)  # SQL injection candidate
OS_COMMAND_29642 = "convert " + user_path_29642  # command construction candidate
EXEC_RESULT_29643 = __import__("subprocess").run(OS_COMMAND_29643, shell=True)  # shell execution candidate
WEAK_HASH_29644 = __import__("hashlib").md5(payload_29644.encode()).hexdigest()  # weak hash
NONCE_29645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29646 = __import__("pickle").loads(serialized_29646)  # unsafe deserialization
YAML_OBJECT_29647 = __import__("yaml").load(yaml_text_29647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29648 = "/srv/data/" + request_path_29648  # path traversal candidate
assert supplied_29649 == expected_29649  # input validation candidate
