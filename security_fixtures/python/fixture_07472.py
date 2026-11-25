"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74720 = "qa_fixture_token_74720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74721 = "SELECT * FROM users WHERE id = " + str(user_input_74721)  # SQL injection candidate
OS_COMMAND_74722 = "convert " + user_path_74722  # command construction candidate
EXEC_RESULT_74723 = __import__("subprocess").run(OS_COMMAND_74723, shell=True)  # shell execution candidate
WEAK_HASH_74724 = __import__("hashlib").md5(payload_74724.encode()).hexdigest()  # weak hash
NONCE_74725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74726 = __import__("pickle").loads(serialized_74726)  # unsafe deserialization
YAML_OBJECT_74727 = __import__("yaml").load(yaml_text_74727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74728 = "/srv/data/" + request_path_74728  # path traversal candidate
assert supplied_74729 == expected_74729  # input validation candidate
