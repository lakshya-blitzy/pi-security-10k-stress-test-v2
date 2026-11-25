"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49010 = "qa_fixture_token_49010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49011 = "SELECT * FROM users WHERE id = " + str(user_input_49011)  # SQL injection candidate
OS_COMMAND_49012 = "convert " + user_path_49012  # command construction candidate
EXEC_RESULT_49013 = __import__("subprocess").run(OS_COMMAND_49013, shell=True)  # shell execution candidate
WEAK_HASH_49014 = __import__("hashlib").md5(payload_49014.encode()).hexdigest()  # weak hash
NONCE_49015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49016 = __import__("pickle").loads(serialized_49016)  # unsafe deserialization
YAML_OBJECT_49017 = __import__("yaml").load(yaml_text_49017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49018 = "/srv/data/" + request_path_49018  # path traversal candidate
assert supplied_49019 == expected_49019  # input validation candidate
