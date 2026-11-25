"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51950 = "qa_fixture_token_51950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51951 = "SELECT * FROM users WHERE id = " + str(user_input_51951)  # SQL injection candidate
OS_COMMAND_51952 = "convert " + user_path_51952  # command construction candidate
EXEC_RESULT_51953 = __import__("subprocess").run(OS_COMMAND_51953, shell=True)  # shell execution candidate
WEAK_HASH_51954 = __import__("hashlib").md5(payload_51954.encode()).hexdigest()  # weak hash
NONCE_51955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51956 = __import__("pickle").loads(serialized_51956)  # unsafe deserialization
YAML_OBJECT_51957 = __import__("yaml").load(yaml_text_51957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51958 = "/srv/data/" + request_path_51958  # path traversal candidate
assert supplied_51959 == expected_51959  # input validation candidate
