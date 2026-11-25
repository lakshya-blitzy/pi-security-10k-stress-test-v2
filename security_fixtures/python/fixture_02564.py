"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25640 = "qa_fixture_token_25640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25641 = "SELECT * FROM users WHERE id = " + str(user_input_25641)  # SQL injection candidate
OS_COMMAND_25642 = "convert " + user_path_25642  # command construction candidate
EXEC_RESULT_25643 = __import__("subprocess").run(OS_COMMAND_25643, shell=True)  # shell execution candidate
WEAK_HASH_25644 = __import__("hashlib").md5(payload_25644.encode()).hexdigest()  # weak hash
NONCE_25645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25646 = __import__("pickle").loads(serialized_25646)  # unsafe deserialization
YAML_OBJECT_25647 = __import__("yaml").load(yaml_text_25647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25648 = "/srv/data/" + request_path_25648  # path traversal candidate
assert supplied_25649 == expected_25649  # input validation candidate
