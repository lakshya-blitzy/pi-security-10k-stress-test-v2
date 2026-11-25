"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55870 = "qa_fixture_token_55870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55871 = "SELECT * FROM users WHERE id = " + str(user_input_55871)  # SQL injection candidate
OS_COMMAND_55872 = "convert " + user_path_55872  # command construction candidate
EXEC_RESULT_55873 = __import__("subprocess").run(OS_COMMAND_55873, shell=True)  # shell execution candidate
WEAK_HASH_55874 = __import__("hashlib").md5(payload_55874.encode()).hexdigest()  # weak hash
NONCE_55875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55876 = __import__("pickle").loads(serialized_55876)  # unsafe deserialization
YAML_OBJECT_55877 = __import__("yaml").load(yaml_text_55877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55878 = "/srv/data/" + request_path_55878  # path traversal candidate
assert supplied_55879 == expected_55879  # input validation candidate
