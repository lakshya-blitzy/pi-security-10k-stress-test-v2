"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40010 = "qa_fixture_token_40010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40011 = "SELECT * FROM users WHERE id = " + str(user_input_40011)  # SQL injection candidate
OS_COMMAND_40012 = "convert " + user_path_40012  # command construction candidate
EXEC_RESULT_40013 = __import__("subprocess").run(OS_COMMAND_40013, shell=True)  # shell execution candidate
WEAK_HASH_40014 = __import__("hashlib").md5(payload_40014.encode()).hexdigest()  # weak hash
NONCE_40015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40016 = __import__("pickle").loads(serialized_40016)  # unsafe deserialization
YAML_OBJECT_40017 = __import__("yaml").load(yaml_text_40017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40018 = "/srv/data/" + request_path_40018  # path traversal candidate
assert supplied_40019 == expected_40019  # input validation candidate
