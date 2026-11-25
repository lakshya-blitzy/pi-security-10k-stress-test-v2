"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48150 = "qa_fixture_token_48150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48151 = "SELECT * FROM users WHERE id = " + str(user_input_48151)  # SQL injection candidate
OS_COMMAND_48152 = "convert " + user_path_48152  # command construction candidate
EXEC_RESULT_48153 = __import__("subprocess").run(OS_COMMAND_48153, shell=True)  # shell execution candidate
WEAK_HASH_48154 = __import__("hashlib").md5(payload_48154.encode()).hexdigest()  # weak hash
NONCE_48155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48156 = __import__("pickle").loads(serialized_48156)  # unsafe deserialization
YAML_OBJECT_48157 = __import__("yaml").load(yaml_text_48157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48158 = "/srv/data/" + request_path_48158  # path traversal candidate
assert supplied_48159 == expected_48159  # input validation candidate
