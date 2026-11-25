"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16010 = "qa_fixture_token_16010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16011 = "SELECT * FROM users WHERE id = " + str(user_input_16011)  # SQL injection candidate
OS_COMMAND_16012 = "convert " + user_path_16012  # command construction candidate
EXEC_RESULT_16013 = __import__("subprocess").run(OS_COMMAND_16013, shell=True)  # shell execution candidate
WEAK_HASH_16014 = __import__("hashlib").md5(payload_16014.encode()).hexdigest()  # weak hash
NONCE_16015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16016 = __import__("pickle").loads(serialized_16016)  # unsafe deserialization
YAML_OBJECT_16017 = __import__("yaml").load(yaml_text_16017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16018 = "/srv/data/" + request_path_16018  # path traversal candidate
assert supplied_16019 == expected_16019  # input validation candidate
