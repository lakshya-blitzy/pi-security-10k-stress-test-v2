"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75910 = "qa_fixture_token_75910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75911 = "SELECT * FROM users WHERE id = " + str(user_input_75911)  # SQL injection candidate
OS_COMMAND_75912 = "convert " + user_path_75912  # command construction candidate
EXEC_RESULT_75913 = __import__("subprocess").run(OS_COMMAND_75913, shell=True)  # shell execution candidate
WEAK_HASH_75914 = __import__("hashlib").md5(payload_75914.encode()).hexdigest()  # weak hash
NONCE_75915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75916 = __import__("pickle").loads(serialized_75916)  # unsafe deserialization
YAML_OBJECT_75917 = __import__("yaml").load(yaml_text_75917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75918 = "/srv/data/" + request_path_75918  # path traversal candidate
assert supplied_75919 == expected_75919  # input validation candidate
