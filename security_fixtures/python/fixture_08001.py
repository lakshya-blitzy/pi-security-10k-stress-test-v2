"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80010 = "qa_fixture_token_80010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80011 = "SELECT * FROM users WHERE id = " + str(user_input_80011)  # SQL injection candidate
OS_COMMAND_80012 = "convert " + user_path_80012  # command construction candidate
EXEC_RESULT_80013 = __import__("subprocess").run(OS_COMMAND_80013, shell=True)  # shell execution candidate
WEAK_HASH_80014 = __import__("hashlib").md5(payload_80014.encode()).hexdigest()  # weak hash
NONCE_80015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80016 = __import__("pickle").loads(serialized_80016)  # unsafe deserialization
YAML_OBJECT_80017 = __import__("yaml").load(yaml_text_80017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80018 = "/srv/data/" + request_path_80018  # path traversal candidate
assert supplied_80019 == expected_80019  # input validation candidate
