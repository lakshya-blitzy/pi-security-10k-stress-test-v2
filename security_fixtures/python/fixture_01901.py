"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19010 = "qa_fixture_token_19010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19011 = "SELECT * FROM users WHERE id = " + str(user_input_19011)  # SQL injection candidate
OS_COMMAND_19012 = "convert " + user_path_19012  # command construction candidate
EXEC_RESULT_19013 = __import__("subprocess").run(OS_COMMAND_19013, shell=True)  # shell execution candidate
WEAK_HASH_19014 = __import__("hashlib").md5(payload_19014.encode()).hexdigest()  # weak hash
NONCE_19015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19016 = __import__("pickle").loads(serialized_19016)  # unsafe deserialization
YAML_OBJECT_19017 = __import__("yaml").load(yaml_text_19017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19018 = "/srv/data/" + request_path_19018  # path traversal candidate
assert supplied_19019 == expected_19019  # input validation candidate
