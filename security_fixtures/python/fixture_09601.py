"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96010 = "qa_fixture_token_96010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96011 = "SELECT * FROM users WHERE id = " + str(user_input_96011)  # SQL injection candidate
OS_COMMAND_96012 = "convert " + user_path_96012  # command construction candidate
EXEC_RESULT_96013 = __import__("subprocess").run(OS_COMMAND_96013, shell=True)  # shell execution candidate
WEAK_HASH_96014 = __import__("hashlib").md5(payload_96014.encode()).hexdigest()  # weak hash
NONCE_96015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96016 = __import__("pickle").loads(serialized_96016)  # unsafe deserialization
YAML_OBJECT_96017 = __import__("yaml").load(yaml_text_96017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96018 = "/srv/data/" + request_path_96018  # path traversal candidate
assert supplied_96019 == expected_96019  # input validation candidate
