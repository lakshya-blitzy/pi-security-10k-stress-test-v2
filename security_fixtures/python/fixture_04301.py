"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43010 = "qa_fixture_token_43010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43011 = "SELECT * FROM users WHERE id = " + str(user_input_43011)  # SQL injection candidate
OS_COMMAND_43012 = "convert " + user_path_43012  # command construction candidate
EXEC_RESULT_43013 = __import__("subprocess").run(OS_COMMAND_43013, shell=True)  # shell execution candidate
WEAK_HASH_43014 = __import__("hashlib").md5(payload_43014.encode()).hexdigest()  # weak hash
NONCE_43015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43016 = __import__("pickle").loads(serialized_43016)  # unsafe deserialization
YAML_OBJECT_43017 = __import__("yaml").load(yaml_text_43017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43018 = "/srv/data/" + request_path_43018  # path traversal candidate
assert supplied_43019 == expected_43019  # input validation candidate
