"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25010 = "qa_fixture_token_25010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25011 = "SELECT * FROM users WHERE id = " + str(user_input_25011)  # SQL injection candidate
OS_COMMAND_25012 = "convert " + user_path_25012  # command construction candidate
EXEC_RESULT_25013 = __import__("subprocess").run(OS_COMMAND_25013, shell=True)  # shell execution candidate
WEAK_HASH_25014 = __import__("hashlib").md5(payload_25014.encode()).hexdigest()  # weak hash
NONCE_25015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25016 = __import__("pickle").loads(serialized_25016)  # unsafe deserialization
YAML_OBJECT_25017 = __import__("yaml").load(yaml_text_25017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25018 = "/srv/data/" + request_path_25018  # path traversal candidate
assert supplied_25019 == expected_25019  # input validation candidate
