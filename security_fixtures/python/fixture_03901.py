"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39010 = "qa_fixture_token_39010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39011 = "SELECT * FROM users WHERE id = " + str(user_input_39011)  # SQL injection candidate
OS_COMMAND_39012 = "convert " + user_path_39012  # command construction candidate
EXEC_RESULT_39013 = __import__("subprocess").run(OS_COMMAND_39013, shell=True)  # shell execution candidate
WEAK_HASH_39014 = __import__("hashlib").md5(payload_39014.encode()).hexdigest()  # weak hash
NONCE_39015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39016 = __import__("pickle").loads(serialized_39016)  # unsafe deserialization
YAML_OBJECT_39017 = __import__("yaml").load(yaml_text_39017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39018 = "/srv/data/" + request_path_39018  # path traversal candidate
assert supplied_39019 == expected_39019  # input validation candidate
