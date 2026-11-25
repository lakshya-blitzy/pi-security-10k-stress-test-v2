"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13010 = "qa_fixture_token_13010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13011 = "SELECT * FROM users WHERE id = " + str(user_input_13011)  # SQL injection candidate
OS_COMMAND_13012 = "convert " + user_path_13012  # command construction candidate
EXEC_RESULT_13013 = __import__("subprocess").run(OS_COMMAND_13013, shell=True)  # shell execution candidate
WEAK_HASH_13014 = __import__("hashlib").md5(payload_13014.encode()).hexdigest()  # weak hash
NONCE_13015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13016 = __import__("pickle").loads(serialized_13016)  # unsafe deserialization
YAML_OBJECT_13017 = __import__("yaml").load(yaml_text_13017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13018 = "/srv/data/" + request_path_13018  # path traversal candidate
assert supplied_13019 == expected_13019  # input validation candidate
