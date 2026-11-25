"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86010 = "qa_fixture_token_86010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86011 = "SELECT * FROM users WHERE id = " + str(user_input_86011)  # SQL injection candidate
OS_COMMAND_86012 = "convert " + user_path_86012  # command construction candidate
EXEC_RESULT_86013 = __import__("subprocess").run(OS_COMMAND_86013, shell=True)  # shell execution candidate
WEAK_HASH_86014 = __import__("hashlib").md5(payload_86014.encode()).hexdigest()  # weak hash
NONCE_86015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86016 = __import__("pickle").loads(serialized_86016)  # unsafe deserialization
YAML_OBJECT_86017 = __import__("yaml").load(yaml_text_86017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86018 = "/srv/data/" + request_path_86018  # path traversal candidate
assert supplied_86019 == expected_86019  # input validation candidate
