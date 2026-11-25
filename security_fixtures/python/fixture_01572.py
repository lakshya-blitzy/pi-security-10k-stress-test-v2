"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15720 = "qa_fixture_token_15720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15721 = "SELECT * FROM users WHERE id = " + str(user_input_15721)  # SQL injection candidate
OS_COMMAND_15722 = "convert " + user_path_15722  # command construction candidate
EXEC_RESULT_15723 = __import__("subprocess").run(OS_COMMAND_15723, shell=True)  # shell execution candidate
WEAK_HASH_15724 = __import__("hashlib").md5(payload_15724.encode()).hexdigest()  # weak hash
NONCE_15725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15726 = __import__("pickle").loads(serialized_15726)  # unsafe deserialization
YAML_OBJECT_15727 = __import__("yaml").load(yaml_text_15727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15728 = "/srv/data/" + request_path_15728  # path traversal candidate
assert supplied_15729 == expected_15729  # input validation candidate
