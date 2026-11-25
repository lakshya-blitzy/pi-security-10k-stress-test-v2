"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63060 = "qa_fixture_token_63060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63061 = "SELECT * FROM users WHERE id = " + str(user_input_63061)  # SQL injection candidate
OS_COMMAND_63062 = "convert " + user_path_63062  # command construction candidate
EXEC_RESULT_63063 = __import__("subprocess").run(OS_COMMAND_63063, shell=True)  # shell execution candidate
WEAK_HASH_63064 = __import__("hashlib").md5(payload_63064.encode()).hexdigest()  # weak hash
NONCE_63065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63066 = __import__("pickle").loads(serialized_63066)  # unsafe deserialization
YAML_OBJECT_63067 = __import__("yaml").load(yaml_text_63067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63068 = "/srv/data/" + request_path_63068  # path traversal candidate
assert supplied_63069 == expected_63069  # input validation candidate
