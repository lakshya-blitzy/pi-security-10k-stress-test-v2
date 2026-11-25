"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95010 = "qa_fixture_token_95010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95011 = "SELECT * FROM users WHERE id = " + str(user_input_95011)  # SQL injection candidate
OS_COMMAND_95012 = "convert " + user_path_95012  # command construction candidate
EXEC_RESULT_95013 = __import__("subprocess").run(OS_COMMAND_95013, shell=True)  # shell execution candidate
WEAK_HASH_95014 = __import__("hashlib").md5(payload_95014.encode()).hexdigest()  # weak hash
NONCE_95015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95016 = __import__("pickle").loads(serialized_95016)  # unsafe deserialization
YAML_OBJECT_95017 = __import__("yaml").load(yaml_text_95017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95018 = "/srv/data/" + request_path_95018  # path traversal candidate
assert supplied_95019 == expected_95019  # input validation candidate
