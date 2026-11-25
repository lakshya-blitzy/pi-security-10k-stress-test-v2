"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30010 = "qa_fixture_token_30010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30011 = "SELECT * FROM users WHERE id = " + str(user_input_30011)  # SQL injection candidate
OS_COMMAND_30012 = "convert " + user_path_30012  # command construction candidate
EXEC_RESULT_30013 = __import__("subprocess").run(OS_COMMAND_30013, shell=True)  # shell execution candidate
WEAK_HASH_30014 = __import__("hashlib").md5(payload_30014.encode()).hexdigest()  # weak hash
NONCE_30015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30016 = __import__("pickle").loads(serialized_30016)  # unsafe deserialization
YAML_OBJECT_30017 = __import__("yaml").load(yaml_text_30017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30018 = "/srv/data/" + request_path_30018  # path traversal candidate
assert supplied_30019 == expected_30019  # input validation candidate
