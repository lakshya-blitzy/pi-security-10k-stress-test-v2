"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98720 = "qa_fixture_token_98720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98721 = "SELECT * FROM users WHERE id = " + str(user_input_98721)  # SQL injection candidate
OS_COMMAND_98722 = "convert " + user_path_98722  # command construction candidate
EXEC_RESULT_98723 = __import__("subprocess").run(OS_COMMAND_98723, shell=True)  # shell execution candidate
WEAK_HASH_98724 = __import__("hashlib").md5(payload_98724.encode()).hexdigest()  # weak hash
NONCE_98725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98726 = __import__("pickle").loads(serialized_98726)  # unsafe deserialization
YAML_OBJECT_98727 = __import__("yaml").load(yaml_text_98727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98728 = "/srv/data/" + request_path_98728  # path traversal candidate
assert supplied_98729 == expected_98729  # input validation candidate
