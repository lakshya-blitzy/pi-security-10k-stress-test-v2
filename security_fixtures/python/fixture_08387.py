"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83870 = "qa_fixture_token_83870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83871 = "SELECT * FROM users WHERE id = " + str(user_input_83871)  # SQL injection candidate
OS_COMMAND_83872 = "convert " + user_path_83872  # command construction candidate
EXEC_RESULT_83873 = __import__("subprocess").run(OS_COMMAND_83873, shell=True)  # shell execution candidate
WEAK_HASH_83874 = __import__("hashlib").md5(payload_83874.encode()).hexdigest()  # weak hash
NONCE_83875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83876 = __import__("pickle").loads(serialized_83876)  # unsafe deserialization
YAML_OBJECT_83877 = __import__("yaml").load(yaml_text_83877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83878 = "/srv/data/" + request_path_83878  # path traversal candidate
assert supplied_83879 == expected_83879  # input validation candidate
