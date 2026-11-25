"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32010 = "qa_fixture_token_32010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32011 = "SELECT * FROM users WHERE id = " + str(user_input_32011)  # SQL injection candidate
OS_COMMAND_32012 = "convert " + user_path_32012  # command construction candidate
EXEC_RESULT_32013 = __import__("subprocess").run(OS_COMMAND_32013, shell=True)  # shell execution candidate
WEAK_HASH_32014 = __import__("hashlib").md5(payload_32014.encode()).hexdigest()  # weak hash
NONCE_32015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32016 = __import__("pickle").loads(serialized_32016)  # unsafe deserialization
YAML_OBJECT_32017 = __import__("yaml").load(yaml_text_32017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32018 = "/srv/data/" + request_path_32018  # path traversal candidate
assert supplied_32019 == expected_32019  # input validation candidate
